import { defineConfig, dynamicImport } from 'umi';

import pageRoutes from './router.config';
import alias from './alias';
import theme from './theme';

import master from './environments/master';
import dev from './environments/dev';
import test from './environments/test';
import pre from './environments/pre';
import online from './environments/online';

var define = dev;
var environment = process.env.NODE_ENV_HUANJING || '本地环境';
if (environment == 'dev') define = dev;
if (environment == 'test') define = test;
if (environment == 'pre') define = pre;
if (environment == 'online') define = online;

if (process.env.NODE_ENV == "development") define = dev;

console.log('--------------------------------------------');
console.log(`--------------当前环境是${environment}----------------`);
console.log('--------------------------------------------');
console.log(define);

let publicPath = process.env.NODE_ENV == "development" ? "/" : "./";

export default defineConfig({
  // 插件配置
  // plugins: ['@umijs/plugin-qiankun'],

  // 设置编译模式
  nodeModulesTransform: {
    type: 'all',
    exclude: [],
  },

  title:"量化",

  publicPath: publicPath,

  history: { type: 'hash' },

  // 静态化 一个路由文件对应一个html文件 (为了百度爬虫以及谷歌爬虫)
  // exportStatic: {},

  //按需加载
  dynamicImport: {},

  // dva
  dva: {},

  // antd
  antd: {},

  //路由配置
  routes: pageRoutes,

  // 国际化配置
  locale: {
    antd: true, // 是否启用antd的<LocaleProvider />  ------由之前的enbale改为 antd
    default: 'zh-CN', //默认语言 zh-CN
    baseNavigator: true, //为true时，用navigator.language的值作为默认语言
    baseSeparator: '-', //语言之间的分隔符
  },

  //多环境配置
  define: define,

  //别名文件的指向
  alias: alias,

  // less变量
  theme: theme,

  //缓存穿透
  hash: true,

  // 配置需要兼容的浏览器最低版本
  targets: {
    ie: 11,
  },

  // 代理
  // proxy: {
  //   '/quant': {
  //     'target': 'http://47.91.251.166:8000',
  //     'changeOrigin': true,
  //     'pathRewrite': { '^/quant' : '' },
  //   },
  // },

});
