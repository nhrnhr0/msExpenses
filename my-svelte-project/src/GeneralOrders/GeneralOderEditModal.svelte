<script>
    export let itemId;
    import {
        Circle
    } from 'svelte-loading-spinners';

    import {
        getCookie
    } from '../utils'
    import {onMount} from 'svelte';
    import {server_create_order,server_get_order,server_update_order} from './GeneralOrdersAPI'
    import {generalOrdersRequestUpdate} from './GeneralOrdersStores'

    let name_input_value;
    let provider_input_value;
    let total_input_value;
    let type_input_value;
    let fields_disabled = false;

    function can_save(name, provider, total, type) {
        console.log('type: ', type);
        if (name && type && provider && total) {
            return true
        }
        return false;
    }
    $: can_svave_reactive = can_save(name_input_value, provider_input_value, total_input_value, type_input_value);
    function get_order() {
        server_get_order(itemId, (result)=>{
            set_order_result(result);
            fields_disabled = false;
        });
    }
    function create_order() {
        fields_disabled = true;
        var formdata = new FormData();
        formdata.append("name", name_input_value);
        formdata.append("providerName", provider_input_value);
        formdata.append("total", total_input_value);
        formdata.append("type", type_input_value);
        server_create_order(formdata, (result)=>{
            set_order_result(result);
            fields_disabled = false;
            generalOrdersRequestUpdate.set(true);
        });
    }

    function update_order() {
    fields_disabled = true;
    var formdata = new FormData();
    formdata.append("id" , itemId);
    formdata.append("name", name_input_value);
    formdata.append("providerName", provider_input_value);
    formdata.append("total", total_input_value);
    formdata.append("type", type_input_value);
    server_update_order(formdata, (result)=>{
            set_order_result(result)
            fields_disabled = false;
            generalOrdersRequestUpdate.set(true);
        })
    }

    function set_order_result(result) {
        itemId = result.id;
        name_input_value = result.name
        provider_input_value = result.providerName;
        total_input_value = result.total;
        type_input_value = result.type;
    }

    onMount(()=> {
        if(itemId) {
            fields_disabled = true;
            get_order()
        }
    })
</script>


<h1>בקשת הזמנת רכש</h1>
<form action="" method="POST">
    {#if itemId}
        <div class="form-group">
            <div>
                מספר סידורי {itemId}
            </div>
        </div>
    {/if}
    <div class="form-group">
        <label for="name">שם:</label>
        <input type="text" disabled={fields_disabled} name="name" bind:value={name_input_value}>
    </div>
    <div class="form-group">
        <label for="provider">ספק:</label>
        <input type="text" name="provider" bind:value={provider_input_value}>
    </div>
    <div class="form-group">
        <label for="total">עלות:</label>
        <input type="text" name="total" bind:value={total_input_value}>
    </div>
    <div class="form-group">
        <label for="type">סוג רכישה:</label>
        <select name="type" bind:value={type_input_value}> 
            <option value=""></option>
            <option value="קבועות">קבועות</option>
            <option value="רכש">רכש</option>
            <option value="ספקים">ספקים</option>
        </select>
    </div>
    {#if fields_disabled}
        <button><Circle size="40" color="#FF3E00" unit="px" duration="1s"></Circle></button>
    {:else}
        {#if can_svave_reactive}
            {#if itemId}
                <button on:click|preventDefault={update_order}>עדכן</button>
            {:else}
                <button on:click|preventDefault={create_order}>צור חדש</button>
            {/if}
        {/if}
    {/if}
</form>