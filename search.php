<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>주소록 입력</title>
</head>
<body>
 <h2>주소록 입력하기</h2><br>
 <form action="./search_process.php" method="post">

 이름:<input type = 'text' name = 'name'><br>
 
 <label for="choices">옵션을 선택하세요:</label>
        <select id="gender" name="gender">
            <option value="option1">모두 출력</option>
            <option value="option2">남자만</option>
            <option value="option3">여자만</option>
        </select>

        <br>
        <input type="submit" value="입력 완료"> 
</form>
</body>
</html>
