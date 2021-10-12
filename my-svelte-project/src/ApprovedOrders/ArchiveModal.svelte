<script>
    import SvelteTooltip from 'svelte-tooltip';

    import { getContext } from 'svelte';
      import ArchiveModalContent from './ArchiveModalContent.svelte';
      export let item;

      const { open } = getContext('simple-modal');
      let mErrors = validateArcive(item);

      function validateArcive(row) {
        let errors = [];
        if(!row.type)   {
            errors.push('סוג הוצאה');
        }
        if(!row.invoiceNumber != '') {
            errors.push('מספר חשבונית');
        }
        if(!row.paid) {
            errors.push('האם שולם');
        }
        if(!row.whenToPay) {
            errors.push('מתי שולם');
        }
        if(!row.paidHow || row.paidHow == 'לא שולם') {
            errors.push('איך שולם');
        }
        if(!row.invoiceLocation || row.invoiceLocation == 'אין חשבונית'){
            errors.push('מיקום חשבונית');
        }
        return errors.join(' ◘ ');
    }
    
      const openArchivedOrderModal = () => {
        open(ArchiveModalContent, {item:item});
      };
    </script>
    <SvelteTooltip tip={mErrors} color="#FFB74D" right>
      {#if mErrors }
        <button disabled >אשר</button>
      {:else}
        <button on:click={openArchivedOrderModal}>אשר</button>
      {/if}
    </SvelteTooltip>