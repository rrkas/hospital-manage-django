from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="inventory-home"),
]

manufacturers = "manufacturers/"
urlpatterns += [
    path(
        manufacturers + "", views.ManufacturerList.as_view(), name="manufacturer-home"
    ),
    path(
        manufacturers + "new/",
        views.ManufacturerCreate.as_view(),
        name="manufacturer-create",
    ),
    path(
        manufacturers + "<int:pk>/",
        views.ManufacturerDetail.as_view(),
        name="manufacturer-detail",
    ),
    path(
        manufacturers + "<int:pk>/update",
        views.ManufacturerUpdate.as_view(),
        name="manufacturer-update",
    ),
]

equipments = "equipments/"
urlpatterns += [
    path(equipments + "", views.EquipmentList.as_view(), name="equipment-home"),
    path(equipments + "new/", views.EquipmentCreate.as_view(), name="equipment-create"),
    path(
        equipments + "<int:pk>/",
        views.EquipmentDetail.as_view(),
        name="equipment-detail",
    ),
    path(
        equipments + "<int:pk>/update",
        views.EquipmentUpdate.as_view(),
        name="equipment-update",
    ),
]
