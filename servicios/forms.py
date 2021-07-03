from django import forms
from .models import *

class municipioForm(forms.ModelForm):
  class Meta:
    model = municipio
    fields = [
      'nombreMunicipio',
      'idEstadoFK']
    labels = {
      'nombreMunicipio': 'Nombre Municipio',
      'idEstadoFK': 'Estado',
      }
    widgets ={
      'nombreMunicipio': forms.TextInput(),
      'idEstadoFK': forms.Select(attrs={'class':'form-control mb-2'}),
      }

class coloniaForm(forms.ModelForm):
  class Meta:
    model = colonia
    fields = [
      'nombreColonia',
      'idMunicipioFK']
    labels = {
      'nombreColonia': 'Nombre Colonia',
      'idMunicipioFK': 'Municipio',
      }
    widgets ={
      'nombreColonia': forms.TextInput(),
      'idMunicipioFK': forms.Select(attrs={'class':'form-control mb-2'}),
      }

class clienteForm(forms.ModelForm):
  def __init__(self,*args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['nombreCliente'].widget.attrs['autofocus'] = True

  class Meta:
    model = cliente
    fields = [
      'nombreCliente',
      'apellidoPaterno',
      'apellidoMaterno',
      'emailCliente',
      'numeroTelefonoUno',
      'numeroTelefonoDos',
      'statusCliente',
      'direccionCliente',
      'idColoniaFK',
      'gpsCliente',
      ]
    labels = {
      'nombreCliente': 'Nombre',
      'apellidoPaterno': 'Apellido paterno',
      'apellidoMaterno': 'Apellido materno',
      'emailCliente': 'Correo electronico',
      'numeroTelefonoUno': 'Numero de Telefono',
      'numeroTelefonoDos': 'Numero de Telefono (opcional)',
      'statusCliente': 'Estatus',
      'direccionCliente': 'Direccion',
      'idColoniaFK': 'Colonia',
      'gpsCliente': 'GPS',
      }
    widgets ={
      'numeroTelefonoDos': forms.TextInput(attrs={'value':'----------'}),
      'gpsCliente': forms.TextInput(attrs={'class':'mb-2'}),
      }

class tecnicoForm(forms.ModelForm):
  class Meta:
    model = tecnico
    fields = [
      'nombreTecnico',
      'apellidoPaterno',
      'apellidoMaterno'
    ]
    labels = {
      'nombreTecnico': 'Nombre',
      'apellidoPaterno': 'Apellido paterno',
      'apellidoMaterno': 'Apellido materno',
    }
    widgets ={
      'nombreTecnico': forms.TextInput(attrs={'class':'form-control'}),
      'apellidoPaterno': forms.TextInput(attrs={'class':'form-control'}),
      'apellidoMaterno': forms.TextInput(attrs={'class':'form-control mb-4'}),
    }
class tarjetaForm(forms.ModelForm):
  class Meta:
    model = tarjeta
    fields = [
      'nombreTarjeta',
      'numeroTarjeta',
      ]
    labels = {
      'nombreTarjeta': 'Nombre de la tarjeta',
      'numeroTarjeta': 'Numero de la tarjeta',
    }
    widgets = {
      'nombreTarjeta': forms.TextInput(attrs={'class':'form-control'}),
      'numeroTarjeta': forms.TextInput(attrs={'class':'form-control mb-4'}),
    }

class servicioForm(forms.ModelForm):
  class Meta:
    model = servicio
    fields = [
      'nombreServicio',
      'descripcionServicio',
      ]
    labels = {
      'nombreServicio': 'Nombre del servicio',
      'descripcionServicio': 'Descripcion del servicio',
    }
    widgets = {
      'nombreServicio': forms.TextInput(attrs={'class':'form-control'}),
      'descripcionServicio': forms.Textarea(attrs={'class':'form-control mb-4'}),
    }

class repetidorForm(forms.ModelForm):
  class Meta:
    model = repetidor
    fields = [
      'fecha',
      'nombreRepetidor',
      'nombreResponsable',
      'numeroTelefonoUno',
      'numeroTelefonoDos',
      'señas',
      'paqueteInternet',
      'ventaMensual',
      'direccionRepetidor',
      'idColoniaFk',
      'gpsRepetidor',
      ]
    labels = {
      'fecha': 'Fecha',
      'nombreRepetidor': 'Nombre del repetidor',
      'nombreResponsable': 'Nombre del responsable',
      'numeroTelefonoUno': 'Telefono',
      'numeroTelefonoDos': 'Telefono (opcional)',
      'señas': 'Señas particulares',
      'paqueteInternet': 'Paquete de internet',
      'ventaMensual': 'Venta mensual',
      'direccionRepetidor': 'Direccion del repetidor',
      'idColoniaFk': 'Colonia',
      'gpsRepetidor': 'GPS',
    }
    widgets ={
      'fecha': forms.SelectDateWidget(attrs={'class':'form-control mb-2'}),
      'nombreRepetidor': forms.TextInput(attrs={'class':'form-control'}),
      'nombreResponsable': forms.TextInput(attrs={'class':'form-control'}),
      'numeroTelefonoUno': forms.TextInput(attrs={'class':'form-control'}), 
      'numeroTelefonoDos': forms.TextInput(attrs={'class':'form-control', 'value':'----------'}), 
      'señas': forms.TextInput(attrs={'class':'form-control'}),
      'paqueteInternet': forms.TextInput(attrs={'class':'form-control'}),
      'ventaMensual': forms.NumberInput(attrs={'class':'form-control'}),
      'direccionRepetidor': forms.TextInput(attrs={'class':'form-control'}),
      'idColoniaFk': forms.Select(attrs={'class':'form-control'}),
      'gpsRepetidor': forms.TextInput(attrs={'class':'form-control mb-4'}),
    }

class reporteForm(forms.ModelForm):
  class Meta:
    model = reporte
    fields = [
      'fechaReporte',
      'descripcionReporte',
      'solucionReporte',
      'costoReporte',
      'tipoPago',
      'observacionesReporte',
      'idTecnicoFK',
      'idClienteFK',
    ]
    labels = {
      'fechaReporte': 'Fecha de reporte',
      'descripcionReporte': 'Descripcion del reporte',
      'solucionReporte': 'Solucion del reporte',
      'costoReporte': 'Costo del reporte',
      'tipoPago': 'Tipo de pago',
      'observacionesReporte': 'Observaciones del reporte',
      'idTecnicoFK': 'Tecnico',
      'idClienteFK': 'Cliente',
    }
    widgets = {
      'fechaReporte': forms.SelectDateWidget(attrs={'class':'form-control mb-2'}),
      'descripcionReporte': forms.Textarea(attrs={'class':'form-control'}),
      'solucionReporte': forms.Textarea(attrs={'class':'form-control'}),
      'costoReporte': forms.NumberInput(attrs={'class':'form-control'}),
      'tipoPago': forms.Select(attrs={'class':'form-control'}),
      'observacionesReporte': forms.Textarea(attrs={'class':'form-control'}),
      'idTecnicoFK': forms.Select(attrs={'class':'form-control'}),
      'idClienteFK': forms.Select(attrs={'class':'form-control mb-4'}),
    }

class gastoEquipoForm(forms.ModelForm):
  class Meta:
    model = gastoEquipo
    fields = [
      'numeroFactura',
      'fecha',
      'statusEquipo',
      'numeroPagos',
      'montoPago',
      'concepto',
      'motivoCompra',
      'nombreProveedor',
      'nombreResponsable',
      'comentarios',
    ]
    labels = {
      'numeroFactura': 'Numero de la factura',
      'fecha': 'Fecha',
      'statusEquipo': 'Estatus del Equipo',
      'numeroPagos': 'Numero de pagos',
      'montoPago': 'Monto por pago',
      'concepto': 'Concepto',
      'motivoCompra': 'Motivo de la compra',
      'nombreProveedor': 'Nombre del proveedor',
      'nombreResponsable': 'Nombre del responsable',
      'comentarios': 'Comentarios',
    }
    widgets = {
      'numeroFactura': forms.NumberInput(attrs={'class':'form-control'}),
      'fecha': forms.SelectDateWidget(attrs={'class':'form-control mb-2'}),
      'statusEquipo': forms.Select(attrs={'class':'form-control'}),
      'numeroPagos': forms.NumberInput(attrs={'class':'form-control'}),
      'montoPago': forms.NumberInput(attrs={'class':'form-control'}),
      'concepto': forms.TextInput(attrs={'class':'form-control'}),
      'motivoCompra': forms.TextInput(attrs={'class':'form-control'}),
      'nombreProveedor': forms.TextInput(attrs={'class':'form-control'}),
      'nombreResponsable': forms.TextInput(attrs={'class':'form-control'}),
      'comentarios': forms.Textarea(attrs={'class':'form-control mb-2'}),
    }

class otrosIngresoForm(forms.ModelForm):
  class Meta:
    model = otrosIngresos
    fields = [
      'numeroNota',
      'fecha',
      'statusIngreso',
      'montoPago',
      'concepto',
      'idClienteFK',
    ]
    labels = {
      'numeroNota': 'Numero de nota',
      'fecha': 'Fecha',
      'statusIngreso': 'Estatus del ingreso',
      'montoPago': 'Monto del Pago',
      'concepto': 'Concepto',
      'idClienteFK': 'Nombre del cliente',
    }
    widgets = {
      'numeroNota': forms.NumberInput(attrs={'class':'form-control'}),
      'fecha': forms.SelectDateWidget(attrs={'class':'form-control mb-2'}),
      'statusIngreso': forms.Select(attrs={'class':'form-control'}),
      'montoPago': forms.NumberInput(attrs={'class':'form-control'}),
      'concepto': forms.TextInput(attrs={'class':'form-control'}),
      'idClienteFK': forms.Select(attrs={'class':'form-control mb-2'}),
    }

class dtaServicioForm(forms.ModelForm):
  class Meta:
    model = detalleServicio
    fields = [
      'fechaDetalle',
      'costoInstalacion',
      'pagoMensual',
      'tipoPago',
      'idServicioFK',
      'idClienteFK',
      'idTecnicoFK',
    ]
    labels = {
      'fechaDetalle': 'Fecha',
      'costoInstalacion': 'Costo de instalacion',
      'pagoMensual': 'Pago mensual',
      'tipoPago': 'Tipo de pago',
      'idServicioFK': 'Servicio',
      'idClienteFK': 'Cliente',
      'idTecnicoFK': 'Tecnico',
    }
    widgets = {
      'fechaDetalle': forms.SelectDateWidget(attrs={'class':'form-control mb-2'}),
      'costoInstalacion': forms.NumberInput(attrs={'class':'form-control'}),
      'pagoMensual': forms.NumberInput(attrs={'class':'form-control'}),
      'tipoPago': forms.Select(attrs={'class':'form-control'}),
      'idServicioFK': forms.Select(attrs={'class':'form-control'}),
      'idClienteFK': forms.Select(attrs={'class':'form-control'}),
      'idTecnicoFK': forms.Select(attrs={'class':'form-control mb-4'}),
    }

class pagosForm(forms.ModelForm):
  class Meta:
    model = pagos
    fields = [
      'folio',
      'nombrePago',
      'fechaPago',
      'montoPago',
      'tipoPago',
      'comentarios',
    ]
    labels = {
      'folio': 'Numero de folio',
      'nombrePago': 'Nombre',
      'fechaPago': 'Fecha',
      'montoPago': 'Monto del Pago',
      'tipoPago': 'Tipo de pago',
      'comentarios': 'Comentarios',
    }
    widgets = {
      'folio': forms.NumberInput(attrs={'class':'form-control'}),
      'nombrePago': forms.TextInput(attrs={'class':'form-control'}),
      'fechaPago': forms.SelectDateWidget(attrs={'class':'form-control mb-2'}),
      'montoPago': forms.NumberInput(attrs={'class':'form-control'}),
      'tipoPago': forms.Select(attrs={'class':'form-control'}),
      'comentarios': forms.Textarea(attrs={'class':'form-control mb-2'}),
    }