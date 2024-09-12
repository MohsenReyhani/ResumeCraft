const swalWithBootstrapButtons1 = Swal.mixin({
	customClass: {
		confirmButton: 'btn btn-primary',
		cancelButton: 'btn btn-gray'
	},
	buttonsStyling: false
});

const Toast = Swal.mixin({
	toast: true,
	position: 'top-start',
	showConfirmButton: false,
	timer: 3000,
	timerProgressBar: true,
	didOpen: (toast) => {
		toast.addEventListener('mouseenter', Swal.stopTimer)
		toast.addEventListener('mouseleave', Swal.resumeTimer)
	}
})


// // SweetAlert 2
// document.getElementById('basicAlert').addEventListener('click', function () {
//   swalWithBootstrapButtons.fire(
//     'Basic alert',
//     'You clicked the button!'
//   )
// });

// document.getElementById('infoAlert').addEventListener('click', function () {
//   swalWithBootstrapButtons.fire(
//     'Info alert',
//     'You clicked the button!',
//     'info'
//   )
// });

// document.getElementById('successAlert').addEventListener('click', function () {
//   swalWithBootstrapButtons.fire({
//     icon: 'success',
//     title: 'Success alert',
//     text: 'Your work has been saved',
//     showConfirmButton: true,
//     timer: 1500
//   })
// });

// document.getElementById('warningAlert').addEventListener('click', function () {
//   swalWithBootstrapButtons.fire(
//     'Warning alert',
//     'You clicked the button!',
//     'warning'
//   )
// });

// document.getElementById('dangerAlert').addEventListener('click', function () {
//   swalWithBootstrapButtons.fire({
//     icon: 'error',
//     title: 'Oops...',
//     text: 'Something went wrong!',
//     footer: '<a href>Why do I have this issue?</a>'
//   })
// });

// document.getElementById('questionAlert').addEventListener('click', function () {
//   swalWithBootstrapButtons.fire(
//     'The Internet?',
//     'That thing is still around?',
//     'question'
//   );
// });

// document.getElementById('notifyTopLeft').addEventListener('click', function () {
//   const notyf = new Notyf({
//     position: {
//       x: 'left',
//       y: 'top',
//     },
//     types: [
//       {
//         type: 'info',
//         background: '#0948B3',
//         icon: {
//           className: 'fas fa-info-circle',
//           tagName: 'span',
//           color: '#fff'
//         },
//         dismissible: false
//       }
//     ]
//   });
//   notyf.open({
//     type: 'info',
//     message: 'Send us <b>an email</b> to get support'
//   });
// });

// document.getElementById('notifyTopRight').addEventListener('click', function () {
//   const notyf = new Notyf({
//     position: {
//       x: 'right',
//       y: 'top',
//     },
//     types: [
//       {
//         type: 'error',
//         background: '#FA5252',
//         icon: {
//           className: 'fas fa-times',
//           tagName: 'span',
//           color: '#fff'
//         },
//         dismissible: false
//       }
//     ]
//   });
//   notyf.open({
//     type: 'error',
//     message: 'This action is not allowed.'
//   });
// });

// document.getElementById('notifyBottomLeft').addEventListener('click', function () {
//   const notyf = new Notyf({
//     position: {
//       x: 'left',
//       y: 'bottom',
//     },
//     types: [
//       {
//         type: 'warning',
//         background: '#F5B759',
//         icon: {
//           className: 'fas fa-exclamation-triangle',
//           tagName: 'span',
//           color: '#fff'
//         },
//         dismissible: false
//       }
//     ]
//   });
//   notyf.open({
//     type: 'warning',
//     message: 'This might be dangerous.'
//   });
// });

// document.getElementById('notifyBottomRight').addEventListener('click', function () {
//   const notyf = new Notyf({
//     position: {
//       x: 'right',
//       y: 'bottom',
//     },
//     types: [
//       {
//         type: 'info',
//         background: '#262B40',
//         icon: {
//           className: 'fas fa-comment-dots',
//           tagName: 'span',
//           color: '#fff'
//         },
//         dismissible: false
//       }
//     ]
//   });
//   notyf.open({
//     type: 'info',
//     message: 'John Garreth: Are you ready for the presentation?'
//   });
// });

function showAlert(status, header, content, footer = "") {
	switch (status) {
		case 'success':
			Toast.fire({
				icon: 'success',
				title: content
			})

			// if (typeof header == 'undefined') {
			// 	header = 'موفقیت!'
			// }
			// swalWithBootstrapButtons1.fire({
			// 	icon: 'success',
			// 	title: header,
			// 	text: content,
			// 	showConfirmButton: true,
			// 	timer: 1500
			// })
			break;
		case 'warning':
			swalWithBootstrapButtons1.fire(
				header,
				content,
				'warning'
			)
			break;
		case 'error':
			swalWithBootstrapButtons1.fire({
				icon: 'error',
				title: header,
				html: content,
				confirmButtonText: 'باشه',
				footer: ((footer != "") ? footer : '<a href="/support">کمک گرفتن از پشتیبانی؟</a>')
			})
			break;
		case 'info':
			swalWithBootstrapButtons1.fire({
				icon: 'info',
				title: header,
				html: content,
				confirmButtonText: 'باشه',
			})
			break;
		default:
			break;
	}
}


function showQuestionAlert(question, warning, yesContent, noContent) {
	return swalWithBootstrapButtons1.fire({
		title: question,
		text: warning,
		icon: 'warning',
		showCancelButton: true,
		confirmButtonColor: '#ab0000',
		cancelButtonColor: '#d33',
		confirmButtonText: yesContent,
		cancelButtonText:
			'<i class="fa fa-thumbs-down">' + noContent + '</i>',
	})
}

async function showOptionsAlert(title, defaultValue, jobPromise) {
	/* inputOptions can be an object or Promise */
	// const inputOptions = new Promise((resolve) => {
	//   setTimeout(() => {
	//     resolve({
	//       '#ff0000': 'Red',
	//       '#00ff00': 'Green',
	//       '#0000ff': 'Blue'
	//     })
	//   }, 1000)
	// })
	return await Swal.fire({

		title: title,
		input: 'select',
		inputOptions: jobPromise,
		confirmButtonText: 'انتخاب',
		inputValue: defaultValue
	})
}

function swalShowLoading(content, isDissmissable) {
	swalWithBootstrapButtons1.fire({
		title: 'چند لحظه ...',
		html: content,
		showConfirmButton: isDissmissable,
		allowOutsideClick: isDissmissable, // Prevents closing by clicking outside
		allowEscapeKey: isDissmissable,    // Prevents closing by pressing the escape key
		allowEnterKey: isDissmissable,
		didOpen: () => {
			swalWithBootstrapButtons1.showLoading()
		}
	});
}
function swalLoadingDone() {
	swalWithBootstrapButtons1.close();
}

function showHint(content) {
	swalWithBootstrapButtons1.fire({
		icon: 'info',
		title: "راهنمایی",
		html: content,
		confirmButtonText: 'باشه',
	})
}

function showCustomDialog(title, html) {
	Swal.fire({
		title: "<strong>" + title + "</strong>",
		icon: "info",
		html: html,
		focusConfirm: false,
		showConfirmButton: false,
	});
}

function showVideoDialog(title, url) {
	var html = '<style>.h_iframe-aparat_embed_frame{position:relative;}.h_iframe-aparat_embed_frame .ratio{display:block;width:100%;height:auto;}.h_iframe-aparat_embed_frame iframe{position:absolute;top:0;left:0;width:100%;height:100%;}</style><div class="h_iframe-aparat_embed_frame"><span style="display: block;padding-top: 57%"></span><iframe src="' + url + '"  allowFullScreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"></iframe></div>'
	Swal.fire({
		title: '<strong>' + title + '</strong>',
		html: html,
		width: '900px',
		padding: '1em',
		background: '#fff',
		showCloseButton: true,
		showConfirmButton: false,
		customClass: {
			popup: 'formatted-popup'
		}
	});
}
// Django messages
// MESSAGE_TAGS = {
// 	messages.DEBUG: 'alert-secondary',
// 	messages.INFO: 'alert-info',
// 	messages.SUCCESS: 'alert-success',
// 	messages.WARNING: 'alert-warning',
// 	messages.ERROR: 'alert-danger',
// }

