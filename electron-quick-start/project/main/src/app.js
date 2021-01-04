import React, { Component } from 'react';
import { history } from 'umi';

/**
 * 比如在最前面添加一个  路由
 */
export function patchRoutes({ routes }) {
  routes.unshift({
    path: '/async',
    exact: true,
    component: require('@/pages/Async/index.js').default,
  });
}

/**
 * 比如用于渲染之前做权限校验，
 */
export function render(oldRender) {
  oldRender();
  // // 模拟走接口
  // setTimeout(() => {
  //   oldRender();
  // }, 2000);
}

/**
 * 在初始加载和路由切换时做一些事情。
 * 比如用于做埋点统计
 * 比如用于设置标题
 */
export function onRouteChange({ location, routes, action }) {
  // console.log(location)   //路由地址
  // console.log(routes)     //全部路由
  // console.log(action)     //跳转动作  push pop 等
}

/**
 * 修改交给 react-dom 渲染时的根组件。
 * 可以做主题切换等等
 */
export function rootContainer(container) {
  return <div className="Theme1">{container}</div>;
}
