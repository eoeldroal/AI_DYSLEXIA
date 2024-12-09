import os
import tempfile
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from home.models import WordExplanation
import threading
import pygame
import sounddevice as sd
from scipy.io import wavfile
from django.http import HttpResponse
import tempfile

# 음성 생성 관련 함수들
def generate_audio_file(text, filename):
    """ 텍스트를 음성 파일로 변환하여 저장 """
    # 예시로 텍스트 음성 생성 API 호출
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )
    with open(filename, "wb") as f:
        f.write(response.content)
    return filename

def play_audio(request, audio_file):
    """ 오디오 파일을 클라이언트에 전송 """
    file_path = os.path.join(settings.MEDIA_ROOT, audio_file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='audio/mp3')
            return response
    return JsonResponse({'error': 'Audio file not found.'}, status=404)

# 단어 설명 조회
def lookup_word_explanation(request, word):
    try:
        explanation = WordExplanation.objects.get(word=word.lower())
        return JsonResponse({
            'word': explanation.word,
            'explanation': explanation.explanation,
            'audio_file': explanation.audio_file.url if explanation.audio_file else None
        })
    except WordExplanation.DoesNotExist:
        return JsonResponse({'error': 'Word not found.'}, status=404)

# 페이지 렌더링
def page_view(request, page_number):
    """ 페이지 요청을 받아 해당 페이지 내용을 렌더링 """
    sentences = get_sentences()  # 문장들 불러오기
    total_pages = len(sentences) + 2  # 전체 텍스트 페이지 + 문제 페이지 포함

    if page_number < 0 or page_number >= total_pages:
        return JsonResponse({'error': 'Page out of range'}, status=404)

    context = {
        'page_number': page_number,
        'sentences': sentences,
        'total_pages': total_pages,
    }

    # 페이지를 렌더링하고 템플릿에 데이터를 전달
    if page_number == total_pages - 2:
        return render(request, 'full_text_page.html', context)
    elif page_number == total_pages - 1:
        return render(request, 'question_page.html', context)
    else:
        return render(request, 'sentence_page.html', context)

# 문제 생성
def generate_question(request):
    sentences = get_sentences()  # 문장들 불러오기
    full_text = " ".join(sentences)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"다음 텍스트를 바탕으로 간단한 질문 하나를 만들어 주세요: {full_text}"}
        ]
    )
    question = response.choices[0].message.content
    return JsonResponse({'question': question})
