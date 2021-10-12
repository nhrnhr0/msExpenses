
<script>
    export let item;
    import { getContext } from 'svelte';
    import {getCookie} from '../utils'
    import {approvedOrdersRequestUpdate} from './ApprovedOrdersStores'
    const { close } = getContext('simple-modal');

    function closeModal() {
        close();
    }

    function archiveItem() {
        const csrftoken = getCookie('csrftoken');
        
        var requestOptions = {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            redirect: 'follow'
        };

        fetch(`archive-ao/${item.id}/`, requestOptions)
            .then(response => response.json())
            .then(result => {
                console.log('result: ', result);
                approvedOrdersRequestUpdate.set(true);
            })
            .catch(error => console.log('error', error));
    }
</script>

<h2>
האם אתה בטוח שברצונך להעביר טופס: {item.id} לארכיון?
</h2>
<h3>
פעולה זאת לא ניתנת לביטול
</h3>
<button on:click={archiveItem}>כן</button>
<button on:click={closeModal}>לא</button>


<style lang="scss">
    h3 {
        color: red;
        text-decoration: underline;
    }
</style>