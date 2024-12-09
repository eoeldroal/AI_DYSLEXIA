import openai
import os

def get_word_explanations_batch(self, words_batch):
        """
        배치 단위로 단어 설명을 요청합니다.
        :param words_batch: 단어 목록 (리스트)
        :return: 단어와 설명의 딕셔너리
        """
        try:
            # 프롬프트 구성: 각 단어에 대한 설명을 요청
            prompt = "다음 한국어 단어들의 간단한 설명을 제공해 주세요. 각 단어과 설명은 '단어: 설명' 형식으로 작성해 주세요.\n\n"
            for word in words_batch:
                prompt += f"{word}\n"
            
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=1500  # 배치 크기에 따라 조정
            )
            explanations_text = response.choices[0].message.content.strip()
            
            # 응답 파싱: '단어: 설명' 형식으로 가정
            explanations = {}
            for line in explanations_text.split('\n'):
                if ':' in line:
                    word, explanation = line.split(':', 1)
                    explanations[word.strip().lower()] = explanation.strip()
            
            return explanations
        except Exception as e:
            print(f"Error fetching explanations for batch: {e}")
            # 실패한 단어에 대한 기본 설명 반환
            return {word.lower(): "설명을 가져오는 데 실패했습니다." for word in words_batch}
