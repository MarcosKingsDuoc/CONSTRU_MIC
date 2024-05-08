def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        carrito = request.session.get("carrito", {})
        for item in carrito.values():
            producto_id = item.get("producto_id")
            cantidad = item.get("cantidad", 0)
            producto = producto.objects.filter(id=producto_id).first()
            if producto:
                total += producto.precio * cantidad
    return {"total_carrito": total}
