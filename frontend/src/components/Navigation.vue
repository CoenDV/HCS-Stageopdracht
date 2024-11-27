<template>
    <div class="container-fluid">
        <header class="d-flex py-2 mb-2 border-bottom">
            <img src="/images/hcs-logo-name.svg" alt="logo" class="img-fluid col-2" />
            <ul class="nav nav-pills mt-3 ms-3 w-100">
                <li class="nav-item">
                    <RouterLink :class="{ disabled: !store.isLoggedIn }" to="/dashboard"
                        class="nav-link link-light text-decoration-underline" active-class="active">
                        Dashboard
                    </RouterLink>
                </li>
                <li class="nav-item">
                    <RouterLink :class="{ disabled: !store.isLoggedIn }" to="/available-documents"
                        class="nav-link link-light text-decoration-underline" active-class="active">
                        Beschikbare Verzekeringen
                    </RouterLink>
                </li>
                <li class="nav-item">
                    <RouterLink :class="{ disabled: !store.isLoggedIn }" to="/account"
                        class="nav-link link-light text-decoration-underline" active-class="active">
                        Account
                    </RouterLink>
                </li>
                <li class="nav-item">
                    <RouterLink :class="{ disabled: !store.isLoggedIn }" to="/logs"
                        class="nav-link link-light text-decoration-underline" active-class="active">
                        Logs (allen voor demo)
                    </RouterLink>
                </li>
                <RouterLink to="/" class="nav-link link-light text-decoration-underline justify-end col-6 text-end"
                    v-if="store.isLoggedIn" @click="handleLogout">Loguit</RouterLink>
            </ul>
        </header>
    </div>
</template>

<script>
import { userStore } from './../stores/userstore';

export default {
    name: "Navigation",
    setup() {
        const store = userStore();

        const handleLogout = () => {
            store.logout();
        }

        return { store, handleLogout };
    },
    data() {
        return {

        }
    }
};
</script>

<style></style>