<template>
	<form class="form shadow-lg rounded bg-white" action="#" @submit.prevent='api_send()'>
		<ul class="">
			<li><label for="login">Ваш логин</label></li>
			<li><input v-model="username" id="login" type="text" name="login" required placeholder="login"></li>
			<li><label for="password">Ваш пароль</label></li>
			<li><input v-model="password" id="password" type="text" name="password" required placeholder="password"></li>
			<li><label for="captcha">Я не робот</label></li>
			<li><input id="captcha" type="checkbox" required></li>
			<li><input type="submit" placeholder="Отправить"></li>
      <li><span>{{ status_info }}</span></li>
		</ul>
	</form>
</template>

<script>

export default {
	name: 'AuthorizationForm',
	components: {
	},
	data() {
		return {
			username: '',
      password: '',
      status_info: '',
		}
	},
	methods: {
		api_send() {
      var axios = require('axios');
      // var FormData = require('form-data');
      // var data = new FormData();

      var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/auth/token/login/',
        mode:'cors',
        // headers: {
          // ...data.getHeaders()
        // },
        data : {
          'username': this.username,
          'password': this.password,
        }
      };


      axios(config)
          .then((response) => {
            this.status_info = JSON.stringify(response.data);
          })
          .catch((error) => {
            this.status_info = error;
          });
		},
	}

}
</script>

<style scoped>
.form {
	width: 350px;
	height: 400px;
}

ul {
	list-style-type: none;
}
</style>
