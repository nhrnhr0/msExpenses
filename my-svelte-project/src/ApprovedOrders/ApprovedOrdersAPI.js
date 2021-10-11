import {getCookie} from '../utils'
export function server_update_order(formdata, on_result, on_error) {
    const csrftoken = getCookie('csrftoken');

    let itemId = formdata.get("id")

    var requestOptions = {
        method: 'PUT',
        headers: {
            'X-CSRFToken': csrftoken
        },
        body: formdata,
        redirect: 'follow'
    };
    console.log('requestOptions: ', requestOptions);
    console.log('itemId: ', itemId);
    debugger;

    fetch(`/api/approved/${itemId}/`, requestOptions)
        .then(response => response.json())
        .then(result => {
            on_result(result);
        })
        .catch(error => {

            console.log('error', error)
            console.log(error);
            on_error(error)
    });
}