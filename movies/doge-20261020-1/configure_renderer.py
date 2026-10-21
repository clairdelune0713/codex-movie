from pathlib import Path
ROOT=Path(__file__).resolve().parent
path=ROOT/'render_finale.py'
s=path.read_text(encoding='utf-8')
s=s.replace('native 480p widescreen','native 480p ultrawide')
s=s.replace("'ratio':'16:9'","'ratio':'21:9'").replace("'aspect_ratio':'16:9'","'aspect_ratio':'21:9'")
s=s.replace('480p 16:9','480p 21:9').replace('native 854x480','native 992x432')
s=s.replace('(854,480)','(992,432)').replace('native_480p_16x9=True','native_480p_21x9=True')
s=s.replace('2026101600','2026102000')
s=s.replace('c[\'chapter_index\']','scene_number(c)')
s=s.replace("p['chapters'][36:51]",'scope_chapters(p)')
s=s.replace("[p['chapters'][int(x)-1] for x in args.chapters.split(',')]","[next(c for c in scope_chapters(p) if scene_number(c)==int(x)) for x in args.chapters.split(',')]")
s=s.replace("checked 2026-10-16",'checked 2026-10-20').replace('https://docs.byteplus.com/en/docs/ModelArk/2191775','https://docs.byteplus.com/en/docs/modelark/model-pricing')
marker='def now():return datetime.now(timezone.utc).isoformat()'
s=s.replace(marker,"def scene_number(c):return c.get('source_scene_number',c['chapter_index'])\ndef scope_chapters(p):\n    result=[c for c in p['chapters'] if 37<=scene_number(c)<=51]\n    if len(result)!=15:raise RuntimeError('Expected exactly15 authorized finale scenes')\n    return result\n\n"+marker)
path.write_text(s,encoding='utf-8')
print('Configured immutable-journal renderer for source scenes37-51 only,480p21:9.')
