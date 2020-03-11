var a = 10;
console.log(a)

function func(){
	/* window.location.href="red.html"  跳转到其他页面 */
	/* window.location.reload(true)  重新加载,加参数true是缓存 */
	window.location.assign("red.html")  /*可以留下历史记录,就是有前进和后退按钮*/
	/* window.location.replace("red.html") /*不会留下历史记录,就是没有前进和后退按钮 */

}