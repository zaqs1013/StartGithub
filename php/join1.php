<!DOCTYPE html>
<html>
    <head>
    <meta charset = 'utf-8'>
    <title>회원 관리 시스템</title>
    </head>
<body>
    <a href = './join1.php'><b><u>회원가입</u></b></a>
    <a href = './search1.php'>회원검색</a>
    <br>
    <h1>회원 가입</h1>

    <form action="./join1_process.php" method="post">
    이름: <input type="text" name="uname" required><br>
    나이: <input type="text" name="uage" required><br>
    성별:
    <input type="radio" name="gender" value="male" required> 남자
    <input type="radio" name="gender" value="female"> 여자<br>
    생년월일: <input type="text" name="birth" required><br><br>
    <input type="submit" value="입력 완료">
</form>

</body>
</html>