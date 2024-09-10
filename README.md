![ERD](https://github.com/user-attachments/assets/f770eb89-eb21-4e23-93ed-cd71fcf28497)

<br>
회원 관련 기능 및 조건

* 회원가입
    * Endpoint: /api/accounts/signup/
    * Method: POST
    * 조건: username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력하며 성별, 자기소개 생략 가능
    * 검증: username과 이메일, nickname 유일해야 하고, 중복 검증
    * 구현: 데이터 검증 후 저장

* 로그인
    * Endpoint: /api/accounts/signin/
    * Method: POST
    * 조건: 유저네임과 비밀번호 입력 필요
    * 검증: 유저네임과 비밀번호가 데이터베이스의 기록과 일치해야 함
    * 구현: 성공적인 로그인 시 토큰을 발급하고, 실패 시 적절한 에러 메시지 반환

* 로그아웃
    * Endpoint: /api/accounts/signout/
    * Method: DELETE
    * 조건: 로그인 상태 필요
    * 구현: 토큰 무효화를 통한 로그아웃 처리

* 프로필 조회
    * Endpoint: /api/accounts/<str:username>
    * Method: GET
    * 조건: 로그인 상태 필요
    * 검증: 로그인 한 사용자만 프로필 조회 가능 (access token)
    * 구현: 로그인한 사용자의 정보를 JSON 형태로 반환 (username, nickname, email, birth, introduction)

<br>
상품 관련 기능 및 조건

* 상품 등록
    * Endpoint: /api/products/
    * Method: POST
    * 조건: 로그인 상태, '제목'과 '내용' 입력 필수, 상품 '이미지' 입력 선택(미입력시 디폴트 이미지 업로드)
    * 구현: 새 게시글 생성 및 데이터베이스 저장

* 상품 목록 조회
    * Endpoint: /api/products/list/
    * Method: GET
    * 조건: 로그인 상태 불필요
    * 구현: 모든 상품 목록 페이지네이션으로 반환

* 상품 수정
    * Endpoint: /api/products/<int:pk>/
    * Method: PUT
    * 조건: 로그인 상태, 수정 권한 있는 사용자(게시글 작성자)만 가능
    * 검증: 요청자가 게시글의 작성자와 일치하는지 확인
    * 구현: 입력된 정보로 기존 상품 정보를 업데이트

* 상품 삭제
    * Endpoint: /api/products/<int:pk>/delete/
    * Method: DELETE
    * 조건: 로그인 상태, 삭제 권한 있는 사용자(게시글 작성자)만 가능
    * 검증: 요청자가 게시글의 작성자와 일치하는지 확인
    * 구현: 해당 상품을 데이터베이스에서 삭제

* 상품 좋아요
    * Endpoint: /api/products/<int:pk>/like/
    * Method: POST
    * 조건: 로그인 상태
    * 구현: Product 모델에 likes 필드 추가 후 ManyToMany 관계 설정
 

API 문서: https://documenter.getpostman.com/view/38042562/2sAXjSyoYf

트러블 슈팅: https://monsterroute.tistory.com/72 