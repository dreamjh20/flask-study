function registerFood(evt) {
    // evt.preventDefault(); /* POST 이벤트 중지 */
    // const foodname = evt.target.foodname.value;
    // const foodsize = evt.target.foodsize.value;
    // if (!foodname || !foodsize) {
    //   return alert('이름과 개수를 모두 입력하세요');
    // }
  
    const email = evt.target.email.value;
    const url = 'http://127.0.0.1:5000';
    const data = { email };
    fetch('/email', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }
  
  document.querySelector('form').addEventListener('submit', registerFood);