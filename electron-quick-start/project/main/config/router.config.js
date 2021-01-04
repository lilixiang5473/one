/**
 * 路由的配置
 */
export default [

  {
    path: '/',
    component: '@/layouts/BasicLayout',
    routes: [

      { path: '/', redirect: '/userLogin' },

      /*****************************登录注册相关******************************/
      // 登录注册
      {
        path: '/userLogin',
        component: '@/layouts/LoginLayout',
        routes: [

          { path: '/userLogin', redirect: '/userLogin/index' },
    
          // 登录页面
          {
            path: '/userLogin/index',
            component: './UserLogin',
            title: '登录',
          },

        ]
      },
      
      /*****************************管理列表页相关******************************/
      {
        path: '/manageList', 
        component:'@/layouts/ManageListLayout',
        routes: [

          { path: '/manageList', redirect: '/manageList/policyManage' },

          /*****************************个人中心相关******************************/
          // 个人中心
          {
            path: '/manageList/userInfo/index',
            component: './UserInfo',
            title: '个人中心',
            hideInMenu: true, // 不展示在左侧导航上面
          },

          {
            path: '/manageList/policyManage',
            title: '策略管理',
            icon: 'iconpeison',
            routes: [

              { path: '/manageList/policyManage', redirect: '/manageList/policyManage/marketMaking' },

              {
                title: '做市策略列表',
                path: '/manageList/policyManage/marketMaking',
                component: './ManageList/PolicyManage/MarketMaking/index',
              },

              {
                title: '交易策略列表',
                path: '/manageList/policyManage/transaction',
                component: './ManageList/PolicyManage/Transaction/index',
              },

              {
                title: '自定义策略列表',
                path: '/manageList/policyManage/custom',
                component: './ManageList/PolicyManage/Custom/index',
              },

              {
                title: '新增做市策略',
                path: '/manageList/policyManage/newMarketMaking',
                component: './ManageList/PolicyManage/NewMarketMaking/index',
              },

              {
                title: '新增交易策略',
                path: '/manageList/policyManage/newTransaction',
                component: './ManageList/PolicyManage/NewTransaction/index',
              },

              {
                title: '新增自定义策略',
                path: '/manageList/policyManage/newCustom',
                component: './ManageList/PolicyManage/NewCustom/index',
              },

            ]

          },

          {
            path: '/manageList/accountAndApi',
            title: '交易账号&API管理',
            style: { letterSpacing: "-0.5px" }, // Menu.SubMenu的样式
            icon: 'iconperson',
            routes: [

              { path: '/manageList/accountAndApi', redirect: '/manageList/accountAndApi/transactionAccount' },

              {
                title: '交易账号管理',
                path: '/manageList/accountAndApi/transactionAccount',
                component: './ManageList/AccountAndApi/TransactionAccount/index',
              },

              {
                title: 'API管理',
                path: '/manageList/accountAndApi/apiManage',
                component: './ManageList/AccountAndApi/ApiManage/index',
              },

            ]

          },

          {
            path: '/manageList/robotManage',
            title: '机器人管理',
            icon: 'iconrobot',
            routes: [

              { path: '/manageList/robotManage', redirect: '/manageList/robotManage/marketMakingRobot' },

              {
                title: '做市机器人列表',
                path: '/manageList/robotManage/marketMakingRobot',
                component: './ManageList/RobotManage/MarketMakingRobot/index',
              },

              {
                title: '交易机器人列表',
                path: '/manageList/robotManage/transactionRobot',
                component: './ManageList/RobotManage/TransactionRobot/index',
              },

              {
                title: '自定义机器人列表',
                path: '/manageList/robotManage/customRobot',
                component: './ManageList/RobotManage/CustomRobot/index',
              },

            ]

          },

          {
            path: '/manageList/reconciliationManage',
            title: '对账管理',
            icon: 'iconrecord',
            routes: [

              { path: '/manageList/reconciliationManage', redirect: '/manageList/reconciliationManage/hedgeReconciliation' },

              {
                title: '对冲对账',
                path: '/manageList/reconciliationManage/hedgeReconciliation',
                component: './ManageList/ReconciliationManage/HedgeReconciliation/index',
              },

            ]

          },

          {
            path: '/manageList/assetsPreview',
            title: '资产一览',
            icon: 'iconwalt',
            component: './ManageList/AssetsPreview/index',
            style: { borderLeft:"5px solid transparent" }, // Menu.Item的样式
            contentStyle: { fontSize:"18px" }, // Link a标签的样式
          },

        ],

      },

      // {
      //   path: '/home',
      //   component: '@/layouts/HomeLayout',
      //   routes: [
      //     { path: '/home', redirect: '/home/index' },
      //     {
      //       title: '首页', // 想要单独设置不同的title在这里 （不设置默认是html文件里的）
      //       // 路由守卫
      //       // wrappers: ['@/pages/Authorized'],
      //       // 路由权限
      //       // authority: ['YYFZJ'],
      //       path: '/home/index',
      //       component: './Home/index',
      //     },
      //     {
      //       title: '我是详情页',
      //       path: '/home/detail/index',
      //       component: './Detail/index',
      //     },
      //   ],
      // },
      
    ],
  },
  
];
