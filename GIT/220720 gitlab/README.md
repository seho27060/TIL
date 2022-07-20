[toc]
# gitlab branch
## branch merge and request
### branch
- 원격 브랜치 : 원격 저장소(repo)에서 생성된 브랜치
- 로컬 브랜치 : 로컬에서만 존재하는 브랜치
#### checkout
- 원격 브랜치를 로컬 브랜치로 `checkout`
```bash
$git checkout -b {생성할 로컬 브랜치 이름} {복사해올 원결 브랜치 이름}
```
- 원격 브랜치를 로컬 브랜치로 복사

#### push
- 커밋 후 {생성한 로컬 브랜치} 러 푸쉬한다

#### merge request
- gitlab 상에서 merge reqeust를 생성하고 리뷰 및 승인후 merge 한다.

#### branch update
- checkout 전 브랜치를 update 해준다.
```bash
$git remote update 
$git branch -r // 원격 저장소 브랜치 확인
$git branch -a // 원격 저장소와 로컬 저장소의 브랜치 확인
```

#### 로컬에서 커밋 취소
-`$git reset HEAD^`