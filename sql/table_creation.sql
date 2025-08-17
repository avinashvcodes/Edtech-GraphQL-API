CREATE TABLE IF NOT EXISTS public.users
(
    id uuid NOT NULL,
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    email character varying(255) COLLATE pg_catalog."default" NOT NULL,
    role character varying(20) COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT users_email_key UNIQUE (email),
    CONSTRAINT role_check CHECK (role::text = ANY (ARRAY['TEACHER'::character varying, 'STUDENT'::character varying, 'ADMIN'::character varying]::text[]))
);


CREATE TABLE IF NOT EXISTS public.courses
(
    id uuid NOT NULL,
    title character varying(200) COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default",
    teacher_id uuid NOT NULL,
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT courses_pkey PRIMARY KEY (id),
    CONSTRAINT unique_title_per_teacher UNIQUE (title, teacher_id),
    CONSTRAINT courses_teacher_id_fkey FOREIGN KEY (teacher_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);


CREATE TABLE IF NOT EXISTS public.sections
(
    id uuid NOT NULL,
    course_id uuid NOT NULL,
    title character varying(200) COLLATE pg_catalog."default" NOT NULL,
    order_index integer NOT NULL,
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT sections_pkey PRIMARY KEY (id),
    CONSTRAINT unique_section_order_per_course UNIQUE (course_id, order_index),
    CONSTRAINT sections_course_id_fkey FOREIGN KEY (course_id)
        REFERENCES public.courses (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS public.lessons
(
    id uuid NOT NULL,
    section_id uuid NOT NULL,
    title character varying(200) COLLATE pg_catalog."default" NOT NULL,
    content text COLLATE pg_catalog."default",
    order_index integer NOT NULL,
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT lessons_pkey PRIMARY KEY (id),
    CONSTRAINT unique_lesson_order_per_section UNIQUE (section_id, order_index),
    CONSTRAINT lessons_section_id_fkey FOREIGN KEY (section_id)
        REFERENCES public.sections (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS public.enrollments
(
    id uuid NOT NULL,
    student_id uuid NOT NULL,
    course_id uuid NOT NULL,
    enrolled_at timestamp without time zone DEFAULT now(),
    CONSTRAINT enrollments_pkey PRIMARY KEY (id),
    CONSTRAINT unique_enrollment UNIQUE (student_id, course_id),
    CONSTRAINT enrollments_course_id_fkey FOREIGN KEY (course_id)
        REFERENCES public.courses (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT enrollments_student_id_fkey FOREIGN KEY (student_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS public.progress
(
    id uuid NOT NULL,
    student_id uuid NOT NULL,
    lesson_id uuid NOT NULL,
    completed boolean,
    completed_at timestamp without time zone,
    CONSTRAINT progress_pkey PRIMARY KEY (id),
    CONSTRAINT unique_student_lesson UNIQUE (student_id, lesson_id),
    CONSTRAINT progress_lesson_id_fkey FOREIGN KEY (lesson_id)
        REFERENCES public.lessons (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT progress_student_id_fkey FOREIGN KEY (student_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
)
