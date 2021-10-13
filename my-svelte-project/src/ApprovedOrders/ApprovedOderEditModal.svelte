<script>
    export let item;
    import {
        Circle
    } from 'svelte-loading-spinners';
    import { Input,Field,Button } from 'svelte-chota';

    import {
        getCookie
    } from '../utils'
    import {onMount} from 'svelte';
    import {server_update_order} from './ApprovedOrdersAPI'
    import {approvedOrdersRequestUpdate} from './ApprovedOrdersStores'

    let formErrors = {}

    let name_input_value;
    let provider_input_value;
    let total_input_value;
    let type_input_value;
    let invoiceNumber_input_value;
    let paidHow_input_value;
    let whenToPay_input_value;
    let invoiceLocation_input_value;
    let paid_input_value;
    let fields_disabled = false;
    
    
    

    function can_save(name, provider, total, type) {
        console.log('type: ', type);
        if (name && type && provider && total) {
            return true
        }
        return false;
    }
    $: can_svave_reactive = can_save(name_input_value, provider_input_value, total_input_value, type_input_value);

    function update_order() {
        fields_disabled = true;
        var formdata = new FormData();
        debugger;
        console.log('whenToPay_input_value: ', whenToPay_input_value);
        console.log('paid_input_value: ', paid_input_value);
        formdata.append("id" , item.id);
        formdata.append("name", name_input_value);
        formdata.append("providerName", provider_input_value);
        formdata.append("total", total_input_value);
        formdata.append("type", type_input_value);
        formdata.append("invoiceNumber", invoiceNumber_input_value);
        formdata.append("paidHow", paidHow_input_value);
        formdata.append('paid', paid_input_value);
        if (whenToPay_input_value) {
            formdata.append("whenToPay", whenToPay_input_value);
        }
        formdata.append("invoiceLocation", invoiceLocation_input_value);


        server_update_order(formdata, (result)=>{
                set_order_result(result)
                fields_disabled = false;
                approvedOrdersRequestUpdate.set(true);

            }, (error)=> {
                formErrors = error;
                alert(error);
            })
    }

    function set_order_result(result) {
        name_input_value = result.name
        provider_input_value = result.providerName;
        total_input_value = result.total;
        type_input_value = result.type;
        invoiceNumber_input_value = result.invoiceNumber;
        paidHow_input_value = result.paidHow;
        whenToPay_input_value = result.whenToPay;
        invoiceLocation_input_value =result.invoiceLocation;
        paid_input_value = result.paid;
    }

    onMount(()=> {
        if(item) {
            fields_disabled = true;
            set_order_result(item)
            fields_disabled = false;
        }
    })
</script>


<h1>בקשת הזמנת רכש</h1>
<form action="" method="POST">
    {#if item}
        <div class="form-group">
            <div>
                מספר סידורי {item.id}
            </div>
        </div>
    {/if}
    <div class="form-group">
        <label for="name">מה תרצו להזמין:</label>
        <Input type="text" disabled={fields_disabled} name="name" bind:value={name_input_value} />
    </div>
    <div class="form-group">
        <label for="provider">ספק:</label>
        <Input type="text" name="provider" bind:value={provider_input_value} />
    </div>
    <div class="form-group">
        <label for="total">עלות כולל מע"מ:</label>
        <Input type="text" name="total" bind:value={total_input_value} />
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
    <div class="form-group">
        <label for="invoiceNumber">מספר חשבונית:</label>
        <input type="text" name="invoiceNumber" bind:value={invoiceNumber_input_value}>
    </div>

    

    <div class="form-group">
        <label for="paidHow">איך תשלום:</label>
        <select name="paidHow" bind:value={paidHow_input_value}> 
            <option value="לא שולם">לא שולם</option>
            <option value="העברה בנקאית">העברה בנקאית</option>
            <option value="דיירקט עידן">דיירקט עידן</option>
            <option value="אשראי אופיר">אשראי אופיר</option>
            <option value="צ'ק נייר">צ'ק נייר</option>
            <option value="מזומן">מזומן</option>
        </select>
    </div>

    <div class="form-group">
        <label for="paid">האם שולם פיזית:</label>
        <input type="checkbox" name="paid" bind:checked={paid_input_value} />
    </div>

    <div class="form-group">
        <label for="whenToPay">תאריך תשלום:</label>
        <Input type="date" name="whenToPay" bind:value={whenToPay_input_value} />
    </div>


    <div class="form-group">
        <label for="invoiceLocation">איפה החשבונית:</label>
        <select name="invoiceLocation" bind:value={invoiceLocation_input_value}> 
            <option value="אין חשבונית">אין חשבונית</option>
            <option value="מסמך בתקייה במחשב">מסמך בתקייה במחשב</option>
            <option value="קובץ נייר במגירה">קובץ נייר במגירה</option>
            <option value="במשלוח פיזי למשרד">במשלוח פיזי למשרד</option>
            <option value="לא ניתן לדיווח">לא ניתן לדיווח</option>
        </select>
    </div>

    

    {#if fields_disabled}
        <button><Circle size="40" color="#FF3E00" unit="px" duration="1s"></Circle></button>
    {:else}
        {#if can_svave_reactive}
            <button on:click|preventDefault={update_order}>עדכן</button>
        {/if}
    {/if}
</form>