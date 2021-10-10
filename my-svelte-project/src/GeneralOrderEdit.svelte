<script>

import { getContext } from 'svelte';
  import GeneralOderEditModal from './GeneralOderEditModal.svelte';
  export let itemId;
  const { open } = getContext('simple-modal');

  const openGeneralOrderModal = () => {
    open(GeneralOderEditModal, {itemId:itemId});
  };
</script>

{#if itemId }
  <p><button on:click={openGeneralOrderModal}>ערוך</button></p>
{:else}
  <p><button on:click={openGeneralOrderModal}>חדש</button></p>
{/if}