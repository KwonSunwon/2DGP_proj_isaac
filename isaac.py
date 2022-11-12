from pico2d import *
import game_framework

import start_state as startState

if __name__ == '__main__':
    open_canvas(1440, 864)
    game_framework.run(startState)
    close_canvas()

# 원래 크기로 해서 안에 타일 크기 변경해서 그리는걸로
# 일어나서 할 일
# 눈물 발싸하는 이펙트 만들기
# 몬스터 이미지만 해서 따라다니는거 만들기
# 맵에 몬스터 배치
# --- 최대한 여기까지는 하기 ---
# 몬스터랑 상호작용 - 부딪히면 데미지, 눈물로 맞추면 데미지