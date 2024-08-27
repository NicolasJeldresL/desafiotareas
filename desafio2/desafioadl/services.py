from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.filter(eliminada=False)
    todas_tareas = []
    for t in tareas:
        tarea_item = {
            'tarea': t,
            'sub_tareas': t.sub_tarea.filter(eliminada=False)
        }
        todas_tareas.append(tarea_item)
    return todas_tareas




def crear_nueva_tarea(descripcion=''):
    tarea = Tarea(descripcion=descripcion, eliminada=False)
    tarea.save()
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, descripcion=''):
    tarea = Tarea.objects.get(pk=tarea_id)
    sub_tarea = SubTarea(descripcion=descripcion, eliminada=False, tarea=tarea)
    sub_tarea.save()
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    tarea.eliminada = True
    tarea.save()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(sub_tarea_id):
    sub_tarea = SubTarea.objects.get(pk=sub_tarea_id)
    sub_tarea.eliminada = True
    sub_tarea.save()
    return recupera_tareas_y_sub_tareas()


def imprimir_en_pantalla(tareas):
    for tarea in tareas:
        print(f'[tarea_id: {tarea["tarea"].id}] {tarea["tarea"].descripcion}')
        for sub in tarea['sub_tareas']:
            print(f'.... [sub_tarea_id: {sub.id}] {sub.descripcion}')

