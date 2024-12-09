# views.py
import os
import pygame
import math
from django.conf import settings  # settings 임포트 추가
from django.shortcuts import render, redirect
from django.http import JsonResponse
from home.models import WordExplanation
import openai
import time


# Pygame 초기화
pygame.init()
pygame.mixer.init()

class WordDatabase:
    def __init__(self, client, splited_text):
        self.client = client
        self.splited_text = splited_text
        self.initialize_database()

    def initialize_database(self):
        # 데이터베이스 초기화는 Django ORM을 사용하므로 따로 작업 필요 없음
        print("Database is configured to use MySQL via Django ORM.")

    def create_database(self):
        # 단어 데이터를 추출하여 데이터베이스에 삽입
        words = self.extract_unique_words()
        print(f"Extracted {len(words)} unique words.")

        batches = self.split_into_batches(words, batch_size=50)  # 배치 크기 조정 가능
        print(f"Processing {len(batches)} batches of words.")

        for i, batch in enumerate(batches, 1):
            print(f"Processing batch {i}/{len(batches)}: {len(batch)} words")
            explanations = self.get_word_explanations_batch(batch)
            audio_files = self.generate_audio_files_batch(batch)
            print("555")
            for word in batch:
                explanation = explanations.get(word.lower(), "설명을 가져오는 데 실패했습니다.")
                audio_file = audio_files.get(word.lower(), None)
                # 단어와 그 설명을 데이터베이스에 저장
                WordExplanation.objects.create(word=word.lower(), audio_file=audio_file, explanation=explanation)
            print(f"Batch {i} processed and saved.")

    def full_text(self):
        return ".".join(self.splited_text)
    
    def split_into_batches(self, words, batch_size=50):
        # 배치 단위로 단어 분할
        words = list(words)
        num_batches = math.ceil(len(words) / batch_size)
        return [words[i * batch_size:(i + 1) * batch_size] for i in range(num_batches)]
    

    def extract_unique_words(self):
        # 텍스트에서 고유 단어 추출
        words = set()

        korean_punctuations = '.,!?~@#$%^&*()_+-={}|[]:;"\'<>?/\\'
        translator = str.maketrans('', '', korean_punctuations)
        for sentence in self.splited_text:
            for word in sentence.split():
                clean_word = word.translate(translator).strip().lower()
                if clean_word:
                    words.add(clean_word)
        return words
     

    def get_word_explanations_batch(self, words_batch):
        # OpenAI API를 통해 단어 설명 요청
        try:

            prompt = "다음 한국어 단어들의 간단한 설명을 제공해 주세요. 각 단어와 설명은 '단어: 설명' 형식으로 작성해 주세요.\n\n"
            for word in words_batch:
                prompt += f"{word}\n"
            print("1111")
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",  # 올바른 모델 이름으로 수정
                messages=[{"role": "system", "content": "You are a helpful assistant."},
                          {"role": "user", "content": prompt}],
                max_tokens=1500,
            )
            print("2222")
            explanations_text = response.choices[0].message["content"].strip()
            print("3333")
            explanations = {}
            for line in explanations_text.split('\n'):
                if ':' in line:
                    word, explanation = line.split(':', 1)
                    print("4444")
                    explanations[word.strip().lower()] = explanation.strip()
                    print("5555")
            return explanations
        
        except Exception as e:
            print(f"Error fetching explanations for batch: {e}")
            # 실패한 단어에 대한 기본 설명 반환
            return {word.lower(): "설명을 가져오는 데 실패했습니다." for word in words_batch}

    def lookup_word_explanation(request, word):
        explanation = WordExplanation.objects.filter(word=word.lower()).first()
        if explanation:
            return JsonResponse({
                'word': explanation.word,
                'explanation': explanation.explanation,
                'audio_file': explanation.audio_file.url if explanation.audio_file else None
            })
