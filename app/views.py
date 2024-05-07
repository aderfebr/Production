from django.http import JsonResponse
from app.models import Node,Edge

# Create your views here.

def getnode(request):
    res=list(Node.objects.all().values())
    return JsonResponse({
        'data':res,
        'code':200,
    })

def addnode(request):
    id=request.POST.get('id')
    description=request.POST.get('description')
    ans=request.POST.get('ans')
    if ans is None:
        ans=0
    else:
        ans=1
    try:
        Node.objects.create(id=id,description=description,ans=ans)
    except:
        return JsonResponse({
            'code':403,
            'msg':'主键重复',
        })
    return JsonResponse({
        'code':200,
    })

def deletenode(request):
    id=request.POST.get('id')
    Node.objects.get(id=id).delete()
    return JsonResponse({
        'code':200,
    })

def getedge(request):
    res=list(Edge.objects.all().values())
    return JsonResponse({
        'data':res,
        'code':200,
    })

def addedge(request):
    node1=request.POST.get('node1')
    node2=request.POST.get('node2')
    try:
        Edge.objects.create(node1=node1,node2=node2)
    except:
        return JsonResponse({
            'code':403,
            'msg':'主键重复',
        })
    return JsonResponse({
        'code':200,
    })

def deleteedge(request):
    id=request.POST.get('id')
    Edge.objects.get(id=id).delete()
    return JsonResponse({
        'code':200,
    })

def forward(request):
    db=set(request.POST.get('judge').split(','))
    f=open('ans.txt','w',encoding='utf-8')
    f.write('已知事实:\n')
    for id in db:
        f.write(Node.objects.get(id=id).description+' ')
    f.write('\n\n推理过程:\n')

    while True:
        last=len(db)
        edges=dict()
        for node in db:
            if Node.objects.get(id=node).ans==True:
                f.write('\n结论:\n'+Node.objects.get(id=node).description)
                break
            res=Edge.objects.filter(node1=node).all().values()
            for tmp in res:
                edges[tmp['node2']]=edges.get(tmp['node2'],0)+1
        for edge in edges.keys():
            cnt=0
            res=Edge.objects.filter(node2=edge).all().values()
            for tmp in res:
                cnt+=1
            if cnt==edges[edge] and str(edge) not in db:
                db.add(str(edge))
                for id in res:
                    f.write(Node.objects.get(id=id['node1']).description+' ')
                f.write('-> '+Node.objects.get(id=edge).description+'\n')
        if len(db)==last:
            break
    f.close()
    return JsonResponse({
        'code':200,
        'msg':'推理完成，请查看本地文件夹下ans.txt文件',
    })

def backward(request):
    def search(node):
        if node in db:
            f.write(Node.objects.get(id=node).description+' 已知\n')
            return 1
        res=Edge.objects.filter(node2=node).all().values()
        if len(res)==0:
            f.write(Node.objects.get(id=node).description+' 未知\n')
            return 0
        ans=1
        for tmp in res:
            ans=ans&search(str(tmp['node1']))
        if ans:
            f.write(Node.objects.get(id=node).description+' 可推出\n')
        else:
            f.write(Node.objects.get(id=node).description+' 无法推出\n')
        return ans
    db=set(request.POST.get('judge').split(','))
    fact=request.POST.get('fact')
    f=open('ans.txt','w',encoding='utf-8')
    f.write('已知事实:\n')
    for id in db:
        f.write(Node.objects.get(id=id).description+' ')
    f.write('\n\n推理过程:\n')
    ans=search(fact)
    if ans:
        f.write('\n假设成立')
    else:
        f.write('\n假设不成立')
    f.close()
    return JsonResponse({
        'code':200,
        'msg':'推理完成，请查看本地文件夹下ans.txt文件',
    })