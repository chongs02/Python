# 표준 입력으로 HTML 태그 이름 두 개가 입력됩니다. 
# 다음 소스 코드에서 함수의 반환값을 HTML 태그로 감싸는 데코레이터를 만드세요. 
# HTML 태그는 웹 페이지에 사용하는 문법이며 <span>문자열</span>, <p>문자열</p>처럼 <태그이름>으로 시작하며 </태그이름>으로 끝납니다.



def html_tag(tag):
    def decorator(func):
        def wrapper():
            return '<{}>{}</{}>'.format(tag,func(),tag)
        return wrapper
    return decorator

a, b = input().split()

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'


print(hello())
