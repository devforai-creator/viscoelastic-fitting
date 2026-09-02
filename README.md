# 점탄성 데이터에 선형 스프링 모델 적용하기

## 이 저장소는 무엇인가

- 시작한 질문: 이전에는 `F=kx`로 표현되는 선형 스프링 모델을 만들어봤는데 이를 실제 신체 조직의 거동을 더 잘 표현하는 모델을 발전시켜보고 싶었다. 
- 이번에 해본 것: 점성 효과가 들어간 가상 데이터를 만들고 단순 스프링 모델로 적합시켰다.
- 확인하고 싶었던 것: 점성 효과가 포함된 데이터를 단순 스프링 모델로 적합하면 어떤 한계가 나타나는가? 이후 댐퍼를 포함한 모델과 비교하고자 한다.

## 파일 구성

- `make_viscoelastic_data.py`: 점성 효과가 들어간 가상 데이터를 생성한다.
- `viscoelastic_test.csv`: 점성 효과가 들어간 테스트용 가상 데이터.
- `estimate_kx_only.py`: 기존 `F=kx`모델로는 어떻게 나타나는지 비교한다.

## 실행 방법

필요한 환경:

- Python
- NumPy
- Matplotlib

실행 순서:

```powershell
python make_viscoelastic_data.py
python estimate_kx_only.py
```