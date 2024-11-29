import { createRouter, createWebHistory } from 'vue-router'

import Login from '@/components/user/Login.vue'
import Dashboard from '@/components/dashboard/Dashboard.vue'
import AvailableDocuments from '@/components/documents/AvailableDocuments.vue'
import account from '@/components/user/Account.vue'
import logs from '@/components/logview/LogOverview.vue'

const router = createRouter({
    history: createWebHistory("/"),
    routes: [
        { path: '/', component: Login },
        { path: '/dashboard', component: Dashboard },
        { path: '/available-documents', component: AvailableDocuments },
        { path: '/account', component: account },
        { path: '/logs', component: logs }
    ]
})

export default router