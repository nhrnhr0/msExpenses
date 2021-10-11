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
  <button on:click={openGeneralOrderModal}>ערוך</button>
{:else}
  <button on:click={openGeneralOrderModal}>חדש</button>
{/if}