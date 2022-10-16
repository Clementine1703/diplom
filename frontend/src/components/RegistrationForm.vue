<template>
	<form class="form shadow-lg rounded bg-white" action="#" @submit.prevent='register()'>
		<ul class="">
			<li><label for="login">Ваш логин</label></li>
			<li><input v-model="username" id="login" type="text" name="login" required placeholder="login"></li>
			<li><label for="password">Ваш пароль</label></li>
			<li><input v-model="password" id="password" type="text" name="password" required placeholder="password"></li>
			<li><label for="captcha">Я не робот</label></li>
			<li><input id="captcha" type="checkbox" required></li>
      <vue-recaptcha
          ref="recaptcha"
          size="visible"
          :sitekey="sitekey"
          @verify="register"
          @expired="onCaptchaExpired"
      />
			<li><input type="submit" placeholder="Отправить"></li>
      <li><span>{{ status_info }}</span></li>
		</ul>
	</form>
</template>

<script>

export default {
	name: 'RegistrationForm',
  data() {
		return {
			username: '123',
      password: '123',
      email:'123@mail.ru',
      status_info: '',
      sitekey: '6LddG4YiAAAAAJ1galXSqpcSFuBvq351uKVuMb6K',
		}
	},
	methods: {
		register() {
      var axios = require('axios');
      // var FormData = require('form-data');
      // var data = new FormData();

      var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/auth/users/',
        mode:'cors',
        // headers: {
          // ...data.getHeaders()
        // },
        data : {
          'username': this.username,
          'password': this.password,
          'email': this.email,
        }
      };


      axios(config)
          .then((response) => {
            if(JSON.stringify(response.status) === '201'){
              this.status_info = 'Вы успешно зарегистрировались!'
            }


          })
          .catch((error) => {
            this.status_info = error.response.data;
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
