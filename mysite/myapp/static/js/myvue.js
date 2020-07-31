// var app = new Vue ({
//   el: '#app',
//   data: {
//     message: 'Hello Vue!'
//   }
// })
//
//
// var app2 = new Vue({
//   el: '#app-2',
//   data: {
//     users: []
//   },
//   created: function(){
//     this.fetchUserList();
//     this.timer = setInterval(this.fetchUserList, 10000);
//   },
//   methods:{
//     fetchUserList: function(){
//       axios.get('/users/').then(response => (this.users = response.data.users))
//       console.log(this.users)
//     },
//     cancelAutoUpdate: function(){clearInterval(this.timer)}
//   },
//   beforeDestroy(){
//     this.cancelAutoUpdate();
//   }
// })
