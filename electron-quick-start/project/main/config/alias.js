/**配置别名指向
 * 这里可以之后根据目录结构配置
 * **/
import path from 'path'
export default{
    "@":path.resolve("src"),
    "@public": path.resolve("public"),
    "@api": path.resolve("src/api"),
    "@services": path.resolve("src/services"),

    "@basicComp":path.resolve("src/components/basicComp"),
    "@businessComp":path.resolve("src/components/businessComp"),
    "@HOC":path.resolve("src/components/HOC"),
}