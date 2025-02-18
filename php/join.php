<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>회원가입 페이지</title>
    <link rel="stylesheet" href="./style1.css">
</head>
<body>
    <div class="form-container">
        <h2>회원가입</h2>
        <form action="./join_process.php" method="post" enctype="multipart/form-data">
            <label for="name">ID:</label>
            <input type="id" id="id" name="id" placeholder="아이디를 입력하세요">
            
            <label for="pw">Password:</label>
            <input type="password" id="pw" name="pw" placeholder="비밀번호를 입력하세요">
            
            <label for="phone">전화번호:</label><br>
            <input type="tel" id="phone" name="phone" placeholder="전화번호를 입력하세요" required><br>
            <br>
            <label for="photo">사진 첨부:</label>
            <input type="file" id="uphoto" name="uphoto">

            <button type="submit">회원가입</button>
        </form>
        <p>회원가입을 완료하면 이용약관에 동의하는 것으로 간주됩니다.<a href = './rogin.php'>로그인</a></p>
    </div>
</body>
</html>