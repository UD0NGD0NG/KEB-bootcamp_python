ls : 현재 폴더에 있는 파일 출력
ls -a : 숨긴 파일도 함께 출력
ls -al : 세부 설명과 함께 출력
touch 파일명 : 폴더에 새로운 파일 생성
rm 파일명 : 폴더에서 해당 폴더 삭제
clear : 내역 삭제

cd 폴더명 : 하위 폴더로 접속(?)

pwd

// 폴더에서 보기 - 숨긴 항목 체크를 통해 .git 파일 노출설정 관리 가능

git 명령어

git config --user.email "mail address" : e-mail 등록 (최초 1회)
git config --user.name "user name" : 유저명 등록 (최초 1회)
git init : 폴더에 .git 추가
git status : 상태 출력
git add 파일명 : 해당 파일을 stage에 올림 (commit을 위한 준비, 파일을 수정할때마다 기록하기 위해서는 add를 항상 해줘야함)
git add . : 모든 파일을 add
git commit -m "내용" : 파일에 내용 저장 (add전에 commit 불가)
git log : commit 기록 출력
git checkout 해시코드 : 해당 버전으로 파일을 설정
git checkout - : 마지막 버전으로 파일을 설정

(end)가 발생시 q누르면 탈출
j : 밑으로, k : 위로

git clone 주소 : 현재 폴더에 주소의 폴더를 폴더채로 가져옴
git clone 주소 . : 현재 폴더에 주소의 폴더안의 파일만 가져옴

git remote -v : 현재 email, user name을 표시
git remote remove origin : git과 github사이의 연결 해제
git remote add origin 리포지토리 주소 : 해당 주소의 github과 현재 파일을 연결

echo "# -" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin 리포지토리 주소
git push -u origin main


readme
<br/> : 줄바꿈
