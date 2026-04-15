# seed.py
from datetime import datetime
from pybo import create_app, db
from pybo.models import Notice

def insert_test_data(n=50):
    """테스트용 질문 데이터 n개 생성"""
    app = create_app()  # Flask 컨텍스트 가 필요
    with app.app_context():
        for i in range(n):
            q = Notice(
                theater='구미점',
                title='테스트 데이터입니다:[%02d]'%i,
                content='내용 없음',
                create_date=datetime.now()
            )
            db.session.add(q)

        db.session.commit()
        print(f'{n}개의 테스트 데이터가 생성되었습니다.')

if __name__ == '__main__':
    insert_test_data()


