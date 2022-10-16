<template>
	<div class="wrapper">
		<site-header></site-header>
		<div class="content-container">
			<authorization-form class="authorization-form position-relative top-50 translate-middle-y">
			</authorization-form>
      <registration-form class="authorization-form position-relative top-50 translate-middle-y"></registration-form>
		</div>

	</div>
</template>

<script>
import SiteHeader from '@/components/SiteHeader.vue';
import AuthorizationForm from '@/components/AuthorizationForm.vue';
import RegistrationForm from "@/components/RegistrationForm";

export default {
	name: 'AuthorizationPage',
	components: {
    RegistrationForm,
		SiteHeader, AuthorizationForm,
	}

}
</script>

<style scoped>
.wrapper {
	margin-top: 56px;
}

.content-container {
	width: 100%;
	height: calc(100vh - 56px);
	background: no-repeat 90%/50% url("@/assets/images/background_auth.jpg");
}

.authorization-form {
	margin-left: 13%;
}
</style>
