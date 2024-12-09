# views.py
from django.shortcuts import render
from django.http import JsonResponse
from home.models import WordExplanation
from .worddatabase import WordDatabase
from django.conf import settings
from openai import OpenAI
import os
import json
import openai
from django.views.decorators.csrf import csrf_exempt

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


# OpenAI 클라이언트를 생성
openai.api_key = OPENAI_API_KEY



@csrf_exempt  # CSRF 인증을 비활성화 (필요 시 사용)
def process_text(request):
    if request.method == 'POST':
        try:
            # JSON 데이터 파싱
            data = json.loads(request.body)
            text = data.get('input_text')  # 사용자로부터 텍스트 입력 받기

            if not text:
                return JsonResponse({'error': '입력된 텍스트가 없습니다.'}, status=400)

            # 텍스트가 None이 아닌 경우만 split()을 호출하도록 수정
            words = text.split(". ")  # 텍스트를 문장 단위로 나누기

            # OpenAI 클라이언트를 통해 단어 데이터베이스를 생성
            word_database = WordDatabase(openai, words)  # SQLite 경로 대신 MySQL 사용

            # 데이터베이스에 저장된 단어 설명들을 가져오기
            words = word_database.extract_unique_words()
            explanations = word_database.get_word_explanations_batch(words)

            # 단어 설명을 JSON 형식으로 반환
            response_data = {
                'words': list(explanations.keys()),
                'explanations': explanations
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({'error': '잘못된 요청 형식입니다.'}, status=400)
    return render(request, 'text.html')  # 기본 화면 반환
