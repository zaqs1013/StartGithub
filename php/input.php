<!DOCTYPE html>
<html lang = "ko">
<head>
    <meta charset = "UTF-8">
    <title>HTML</title>
</head>
<body>
<fieldset style= 'width:500px; background:skyblue;'>
<legend align="left" style="color: red;">다이어트</legend>
    <form action = './test.php' method='post' autocomplete = 'off'>
        키: <input type = 'text' name='key'><br>
        몸무게: <input type = 'text' name='mo'><br>
        <input type = 'submit' value = '저장하기'>
    </form>
</fieldset>
    <br><br>

    <form action = './test2.php' method = 'post'>
    <br><br>

    <fieldset style= 'width:500px; background:skyblue;'>
    <legend align="left" style="color: red;">놀이공원 입장료 계산기</legend>
        <h3>야간에는 20% 할인 혜택이 적용됩니다.</h3>
        <label for= 'num'>인원수:</label>
        <select name= 'num' id= 'num'>
            <option value= '1'>1명</option>
            <option value= '2'>2명</option>
            <option value= '3'>3명</option>
            <option value= '4'>4명</option>
            <option value= '5'>5명</option>
        </select>
        
        <label for= 'age'>연령:</label>
        <select name= 'age' id= 'age'>
            <option value= '1'>대인(18세 이상)</option>
            <option value= '2'>청소년(7~17세)</option>
            <option value= '3'>유아(7세 미만)</option>

        </select>

    <br><br>
    <label for= 'time'>입장 시간: </label>
    <input type='radio' name='time' value='t1'>오전 시간대
    <input type='radio' name='time' value='t2'>오후 시간대
    <input type='radio' name='time' value='t3'> 야간 시간대

    <br><br>
    <input type = 'submit' value = '전송'>
    </fieldset>

    </form>

</body>
</html>
