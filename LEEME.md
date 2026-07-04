# KISpec — Keep It Simple, spec

*Sobre Spec-Driven Development, y cuánta hace falta de verdad.*

Como nos pasa con el overengineering... si te pasas caes en el **over-specification**. Lo único que necesitas de verdad es la expectativa "vaga" (el **qué**, el **por qué** y el **para qué**), los tests para validar ese requisito claramente (el TDD de toda la vida, pero a nivel de proyecto, que es lo bueno que aporta SDD o más concretamente Kiro) y, obviamente, el bucle para afinar el resultado. **KISS.**

A esto le puedes añadir tus reglas de cómo hacer el trabajo con un `AGENTS.md` para motorizar/controlar el proceso (PRs, ficheros de reporte o incluso gestión de tickets de Jira). Pero cuidado: **cada control es un bloqueo en el trabajo de la IA.**

He desarrollado —bueno, yo solo *pido* 😄— proyectos complejísimos partiendo de unas simples "expectativas" de lo que quiero y luego afinando el resultado con más "expectativas". Todas estas rigideces no aportan mucho si el modelo es suficientemente bueno (y Fable ya tiene mejor criterio y más "experiencia" de cómo hacer el proyecto que tú). Tu opinión aporta poco, salvo para acortar el bucle y acercarte a tus expectativas más rápido y con menos tokens; es más, muchas veces lo *limita*, porque le impide llegar a mejores soluciones.

Como siempre, el diablo está en los detalles, y los detalles casi siempre se descubren **durante la implementación**. Esta metodología te ayuda a estructurar el trabajo si tú mismo no sabes muy bien lo que quieres, pero al final te das cuenta de que casi siempre terminas poniendo el `"sdd": false` porque todo es demasiado sencillo y se resuelve con unos simples prompts. **YAGNI.**

> *`"sdd"` es el flag por feature de [harness-sdd](https://github.com/betta-tech/harness-sdd):
> una feature marcada `true` en su `feature_list.json` debe pasar por una fase de spec antes
> de tocar código. Mi tesis es que la mayoría deberían ir en `false` — y este repo es el
> esqueleto para las pocas que no.*

---

## El matiz: el debate no es SDD sí/no, es *cuánta*

Que quede claro: mi propia receta —**expectativa vaga + tests + bucle**— *ya es* SDD, solo que mínimo. Así que la pregunta real nunca fue "¿spec o no spec?", sino **"¿cuánta spec?"**. Y esa cantidad no es fija: depende de lo que te juegas.

La spec **sí se gana el sueldo** cuando:

- **El coste de equivocarse es alto e irreversible.** Migraciones de datos, APIs públicas con consumidores enganchados, dominios regulados. Ahí el "ya lo afino luego" sale caro: no hay bucle barato.
- **El proyecto sobrevive a una sola conversación.** Cuando lo retomas en tres meses, o lo coge otra persona (u otro agente), la spec es la memoria que queda. El chat se pierde; el contexto se evapora.
- **Hay más de un actor.** Ahí la spec deja de ser humano→IA y pasa a ser el **contrato compartido** entre personas y agentes. Eso no es burocracia, es sincronización.

Para todo lo demás —que es la mayoría de lo que hago— sobra.

## Spec durable vs. ceremonia

No todas las specs son iguales, y aquí está la trampa. Los **tests son specs ejecutables**: persisten, atrapan regresiones, no mienten. La **prosa se pudre** en cuanto la implementación avanza dos pasos. Por eso defiendo el TDD a nivel de proyecto y desconfío de los tres `.md` ceremoniales.

El problema nunca fue *especificar*. El problema es especificar en un formato que **hay que mantener a mano** y que nadie vuelve a mirar.

## El "por qué" es lo único que no caduca

El diablo está en los detalles y los detalles se descubren implementando: cierto. Por eso el **cómo** de una spec envejece fatal, y por eso escribirlo por adelantado suele ser tirar tokens. Pero el **qué** y el **por qué** —mi "expectativa vaga"— son justo lo que **nunca queda obsoleto** y lo que un modelo bueno, por listo que sea, **no puede adivinar**.

Ese es el núcleo irreductible de la spec: conserva el porqué, tira el cómo.

(No todo *porqué* cuenta igual — los que un modelo puede adivinar son justo los que *no* escribes. Ver [`NOTE-FROM-CLAUDE.md`](NOTE-FROM-CLAUDE.md) para la distinción convencional-vs-contingente que mantiene honesta esta afirmación.)

## El "para qué" puede jubilar el proyecto entero

Hay un matiz dentro de esa "expectativa vaga" que conviene separar. El **por qué** justifica *cómo* está hecho; el **para qué** justifica que el proyecto *exista siquiera*. Y ese último no es un asunto de implementación — es un asunto de SDLC que sobrevive a cada línea de código.

Porque el "para qué" es lo que revisas a lo largo de toda la vida del proyecto, y un día la respuesta honesta es "ese para qué ya no existe". El mercado cambió, el sistema del que dependía lo reemplazaron, cambió la normativa, mataron la funcionalidad a la que alimentaba. Cuando eso pasa, lo correcto no es seguir manteniéndolo, refactorizándolo ni re-especificándolo — es **jubilarlo**. YAGNI a escala de proyecto: el código más barato es el que borras porque su razón de ser ha desaparecido. Una spec que nunca anotó el "para qué" no puede decirte cuándo toca dejar morir el proyecto.

## Registra las decisiones del camino: ADRs

Y aquí está la pieza que lo cierra todo. Si el diablo está en los detalles y los detalles aparecen **durante** la implementación, entonces las decisiones que de verdad importan **no estaban en la spec inicial**: nacen por el camino. "Usamos esta librería y no aquella", "elegimos consistencia eventual aquí", "descartamos el enfoque X porque Y". Cada una de esas es una bifurcación con un porqué detrás.

Ese porqué es exactamente lo que se evapora cuando se cierra la conversación. El código te dice *qué* se hizo; jamás te dice *qué se descartó ni por qué*. Y el "por qué no" suele ser más valioso que el "qué", porque es lo que evita que dentro de seis meses alguien —tú, otra persona o un agente— rehaga el mismo debate desde cero o reintroduzca el error que ya descartaste.

Por eso, **toda decisión relevante tomada por el camino debería quedar registrada en un ADR** (Architecture Decision Record) que acompañe a la documentación habitual del proyecto. Cortos, uno por decisión: contexto, opción elegida, alternativas descartadas y el porqué. Nada de ceremonia — son el registro incremental del criterio, no un documento que haya que mantener sincronizado con el código. Un ADR no miente porque no promete estar al día: fecha una decisión y su razón, y ahí se queda.

Esto es lo que convierte al proyecto en algo que **sobrevive a una sola conversación**: la spec inicial captura el qué y el porqué de partida; los ADRs capturan el porqué de todo lo que se descubrió después.

---

## El esqueleto

Este repo *es* el método. La estructura es sobre todo ausencia — y esa es la gracia:

```
kispec/
├── EXPECTATIONS.md   # el qué / por qué / para qué — la "expectativa vaga"
├── tests/            # la spec ejecutable (TDD a nivel proyecto)
├── decisions/        # ADRs: el porqué de todo lo descubierto por el camino
│   ├── template.md
│   └── 0001-....md
├── AGENTS.md         # el único control opcional (tus reglas de proyecto)
└── CLAUDE.md         # una línea — `@AGENTS.md` — para que las reglas valgan en cualquier agente
```

> Las reglas viven en `AGENTS.md` (el estándar entre herramientas). `CLAUDE.md`
> solo lo importa con `@AGENTS.md`, así Claude Code, Codex, Cursor y compañía leen
> el mismo fichero — sin duplicar. (Truco robado al autor de t3code.)

Lo que deliberadamente **no** está, y por qué:

- sin `design.md` — el *cómo* es trabajo del modelo y es lo que antes envejece; escribirlo por adelantado es tirar tokens.
- sin `tasks.md` — una checklist congelada pelea contra el bucle; el bucle es la lista de tareas, y está viva.
- sin documento formal de requisitos — eso vive en grueso en `EXPECTATIONS.md` y en preciso en `tests/`.

Es Kiro / Spec Kit con el dial bajado, y OpenSpec (que ya trae los ADRs dentro de sus
change proposals) bajado un punto más. Si
[harness-sdd](https://github.com/betta-tech/harness-sdd) es el extremo máximo de ese
dial — una fase de spec en cada feature —, KISpec es el extremo mínimo: el mismo dial,
el tope opuesto. El porqué está en
[`decisions/0001-keep-the-skeleton-minimal.md`](decisions/0001-keep-the-skeleton-minimal.md)
— un ADR, cómo no.

## La regla

> La spec no es el entregable, es andamiaje. Pon el andamio **proporcional a la altura de la caída**: cuanto más caro sea equivocarse, o más gente y más tiempo tenga que sobrevivir el proyecto, más spec. Para todo lo demás, `"sdd": false` y un buen prompt.
