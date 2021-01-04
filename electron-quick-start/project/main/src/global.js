import '@/styles/index.less';                     // 引入自定义样式的汇集入口文件
import { setLocale } from 'umi';
import moment from 'moment';
import 'moment/locale/zh-cn';
import '@public/iconfont/iconfont.js';
import _ from "lodash";

var locale = localStorage.getItem('locale') || 'zh-CN'
moment.locale(locale.toLowerCase())
setLocale(locale)
