import {getCookie} from '../utils'


export function server_get_order(itemId, on_result) {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    fetch(`/api/general/${itemId}`, requestOptions)
        .then(response => response.json())
        .then(result => {
            on_result(result);
            
        })
        .catch(error => console.log('error', error));
}


export function server_create_order(formdata, on_result) {
    const csrftoken = getCookie('csrftoken');



    var requestOptions = {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        body: formdata,
        redirect: 'follow'
    };

    fetch("/api/general/", requestOptions)
        .then(response => response.json())
        .then(result => {
            on_result(result)
        })
        .catch(error => console.log('error', error));
}


export function server_update_order(formdata, on_result) {
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

    fetch(`/api/general/${itemId}/`, requestOptions)
        .then(response => response.json())
        .then(result => {
            on_result(result);
        })
        .catch(error => console.log('error', error));
}