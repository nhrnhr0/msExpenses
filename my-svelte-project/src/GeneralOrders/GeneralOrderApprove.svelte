<script>

    import { getContext } from 'svelte';
      import GeneralOrderApproveModal from './GeneralOrderApproveModal.svelte';
      export let itemId;
      import {getCookie} from '../utils'

      const { open } = getContext('simple-modal');
      function onCancel() {

      }

      function onOkey() {
        const csrftoken = getCookie('csrftoken');
        
        var requestOptions = {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            redirect: 'follow'
        };

        fetch(`approve-go/${itemId}/`, requestOptions)
            .then(response => response.json())
            .then(result => {
                console.log('result: ', result);
            })
            .catch(error => console.log('error', error));
      }
    
      const openApproveModal = () => {
        open(GeneralOrderApproveModal, {itemId:itemId,onOkey, onCancel});
      };
    </script>

    <button on:click="{openApproveModal}">אשר</button>