<script>

    import { getContext } from 'svelte';
      import ApprovedOderEditModal from './ApprovedOderEditModal.svelte';
      export let item;
    
      const { open } = getContext('simple-modal');
    
      const openApprovedOrderModal = () => {
        open(ApprovedOderEditModal, {item:item});
      };
    </script>
    
    {#if item }
      <button on:click={openApprovedOrderModal}>ערוך</button>
    {:else}
      <button on:click={openApprovedOrderModal}>חדש</button>
    {/if}