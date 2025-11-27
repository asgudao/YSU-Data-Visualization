import axios from 'axios';

const service = axios.create({
    baseURL: 'http://127.0.0.1:5000',  // 你的 Flask 地址
    timeout: 5000
});

// 拦截请求
service.interceptors.request.use(
    config => {
        return config;
    },
    error => Promise.reject(error)
);

// 拦截响应
service.interceptors.response.use(
    response => response.data,
    error => Promise.reject(error)
);

export default service;
