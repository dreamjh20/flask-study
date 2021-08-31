import Axios from 'axios';

console.log("JS BEGIN")

axios.get('/language', {
    params: {
      language: 'C++'
    }
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  })
  .finally(function () {
      console.log('finally')
  });