// {
//   tag: 'DIV',
//   attrs:{
//   id:'app'
//   },
//   children: [
//     {
//       tag: 'SPAN',
//       children: [
//         { tag: 'A', children: [] }
//       ]
//     },
//     {
//       tag: 'SPAN',
//       children: [
//         { tag: 'A', children: [] },
//         { tag: 'A', children: [] }
//       ]
//     }
//   ]
// }
// 把上诉虚拟Dom转化成下方真实Dom
// <div id="app">
//   <span>
//     <a></a>
//   </span>
//   <span>
//     <a></a>
//     <a></a>
//   </span>
// </div>

function _render(vnode) {
  if (typeof vnode === "number") return String(vnode);
  if (typeof vnode === "string") return document.createTextNode(vnode);

  const dom = document.createElement(vnode.tag);
  if (vnode.attrs) {
    for (const key of Object.keys(vnode.attrs)) {
      const val = vnode.attrs[key];
      dom.setAttribute(key, val);
    }
  }

  for (const child of vnode.children) {
    dom.appendChild(_render(child));
  }
  return dom;
}
