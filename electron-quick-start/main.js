// Modules to control application life and create native browser window
const {app, BrowserWindow, Menu} = require('electron')
const path = require('path')

function createWindow () {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 1250,
    height: 800,
    minWidth: 800,
    minHeight: 700,
    webPreferences: { // 预加载配置
      nodeIntegration:true, // 预加载的时候添加node环境给内嵌应用
      preload: path.join(__dirname, 'preload.js'), // 预加载的js文件
    }
  })

  // 入口域名(开发环境)
  mainWindow.loadURL('http://localhost:8000')

  // 入口文件(打包环境)
  // mainWindow.loadFile(path.join(__dirname, 'project/main/dist/index.html'));

  // 可以操作本文资源的权限，不只是沙盒环境
  // const fs = require('fs')
  // const root = fs.readdirSync('/')
  // console.log(root);

  // 远程
  // mainWindow.loadURL('https://www.3q5k68.cn/ex')

  // 打开开发者工具
  mainWindow.webContents.openDevTools();
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', function () {
  // mac 系统可以快捷键关闭应用，所以判断下，快捷键关掉了也要停止应用
  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', function () {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) createWindow();
})

// 底部右键的菜单栏(Windows独有)
app.setUserTasks([
  {
    program: process.execPath,
    arguments: '--new-window',
    iconPath: process.execPath,
    iconIndex: 0,
    title: 'New Window',
    description: 'Create a new window'
  }
])

// 底部右键的菜单栏(MacOS独有)
// const dockMenu = Menu.buildFromTemplate([
//   {
//     label: 'New Window',
//     click () { console.log('New Window') }
//   }, {
//     label: 'New Window with Settings',
//     submenu: [
//       { label: 'Basic' },
//       { label: 'Pro' }
//     ]
//   },
//   { label: 'New Command...' }
// ])

// app.dock.setMenu(dockMenu)

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
