<template>
    <div class="container-fluid">
        <header class="d-flex py-2 mb-2 border-bottom">
            <img src="/images/hcs-logo-name.svg" alt="logo" class="img-fluid col-2" />
            <ul class="nav nav-pills mt-3 ms-3 w-100">
                <li class="nav-item">
                    <RouterLink to="/dashboard" class="nav-link link-light text-decoration-underline"
                        active-class="active">
                        Dashboard
                    </RouterLink>
                </li>
                <li class="nav-item">
                    <RouterLink to="/available-documents" class="nav-link link-light text-decoration-underline"
                        active-class="active">
                        Beschikbare Verzekeringen
                    </RouterLink>
                </li>
                <li class="nav-item">
                    <RouterLink to="/account" class="nav-link link-light text-decoration-underline"
                        active-class="active">
                        Account
                    </RouterLink>
                </li>
                <a href="#" class="nav-link link-light text-decoration-underline justify-end col-8 text-end">Loguit</a>
            </ul>
        </header>
    </div>
</template>

<script>

export default {
    name: "Navigation",
    setup() {

    },
    data() {
        return {

        }
    }
};
</script>

<style></style>