<template>
    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
      aria-expanded="false">
        Аккаунт
    </a>
    <ul class="dropdown-menu">
      <li><router-link :to="{name: 'profile'}" class="dropdown-item">Профиль</router-link></li>
      <li><a class="dropdown-item" href="#">Настройки</a></li>
      <li>
        <hr class="dropdown-divider">
      </li>
      <li><a class="dropdown-item" href="#" @click.prevent="logout()">Выход</a></li>
    </ul>

</template>



<script>
export default {
  name: 'SmallProfile',
  components:{},
  methods:{
    logout(){
      this.$store.state.status.auth = false;
      this.$store.state.status.auth_token = '';
      this.$cookies.remove('auth_token');
      this.$router.push({name: 'authentication'});
      // this.$cookies.remove('auto_login');
      // this.$cookies.remove('auto_password');
    }
  }

}

</script>


<style scoped>

.small-profile{
  width: 24px;
  height: 24px;
  background-color: #0f0f0f;
}

</style>