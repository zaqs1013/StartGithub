<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>회원가입 페이지</title>
    <link rel="stylesheet" href="./style1.css">
</head>
<body>
    <div class="form-container">
        <h2>로그인</h2>
        <form action="./rogin_process.php" method="post">
            <label for="name">ID:</label>
            <input type="id" id="id" name="id" placeholder="아이디를 입력하세요">
            
            <label for="pw">Password:</label>
            <input type="password" id="pw" name="pw" placeholder="비밀번호를 입력하세요">

            <button type="submit" value = 'LOGIN'>로그인</button>
        </form>
        <p>아직 회원가입을 안하셨나요? <a href = './join.php'>회원가입 </a></p>
    </div>
</body>
</html>